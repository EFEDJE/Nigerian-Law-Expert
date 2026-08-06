import re

from app.rag.models import Page, Section


class LegalParser:
    CHAPTER_PATTERN = re.compile(r"^CHAPTER\s+[IVXLCDM]+$", re.IGNORECASE)
    PART_PATTERN = re.compile(r"^PART\s+[IVXLCDM]+$", re.IGNORECASE)

    # Matches: "45. Restriction on Rights"
    SECTION_PATTERN = re.compile(r"^(\d+)\.\s*(.+)$")

    # Matches: "45."
    SECTION_NUMBER_ONLY = re.compile(r"^(\d+)\.$")

    def __init__(self, start_page: int = 23, end_page: int = 214):
        self.start_page = start_page
        self.end_page = end_page

    def parse(self, pages: list[Page]) -> list[Section]:

        sections = []

        current_chapter = None
        current_part = None
        current_section = None

        expecting_section_title = False
        pending_article = None

        for page in pages:

            if page.page < self.start_page:
                continue

            if page.page > self.end_page:
                break

            for line in page.lines:

                line = line.strip()

                if not line:
                    continue

                # ---------------------------------
                # Remove page headers / footers
                # ---------------------------------

                if line.isdigit():
                    continue

                if "The Constitution of the Federal Republic" in line:
                    continue

                if "Updated with the" in line:
                    continue

                # ---------------------------------
                # CHAPTER
                # ---------------------------------

                if self.CHAPTER_PATTERN.match(line):

                    current_chapter = line
                    continue

                # ---------------------------------
                # PART
                # ---------------------------------

                if self.PART_PATTERN.match(line):

                    current_part = line
                    continue

                # ---------------------------------
                # SECTION (Number + Title)
                # Example:
                # 45. Restriction on Rights
                # ---------------------------------

                section_match = self.SECTION_PATTERN.match(line)

                if section_match:

                    if current_section:
                        sections.append(current_section)

                    current_section = Section(
                        chapter=current_chapter,
                        part=current_part,
                        article=int(section_match.group(1)),
                        section_title=section_match.group(2).strip(),
                        page=page.page,
                        text=""
                    )

                    continue

                # ---------------------------------
                # SECTION NUMBER ONLY
                # Example:
                # 45.
                # ---------------------------------

                number_match = self.SECTION_NUMBER_ONLY.match(line)

                if number_match:

                    if current_section:
                        sections.append(current_section)

                    pending_article = int(number_match.group(1))
                    expecting_section_title = True

                    continue

                # ---------------------------------
                # NEXT LINE IS THE SECTION TITLE
                # ---------------------------------

                if expecting_section_title:

                    current_section = Section(
                        chapter=current_chapter,
                        part=current_part,
                        article=pending_article,
                        section_title=line,
                        page=page.page,
                        text=""
                    )

                    expecting_section_title = False
                    pending_article = None

                    continue

                # ---------------------------------
                # BODY
                # ---------------------------------

                if current_section:
                    current_section.text += line + " "

        # Save the last section
        if current_section:
            current_section.text = " ".join(current_section.text.split())
            sections.append(current_section)

        return sections