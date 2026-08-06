from dataclasses import dataclass
import numpy as np


@dataclass
class Page:
    page: int
    lines: list[str]


@dataclass
class Section:
    chapter: str | None
    part: str | None
    article: int
    section_title: str | None
    page: int
    text: str


@dataclass
class Chunk:
    chunk_id: int
    document: str
    chapter: str | None
    part: str | None
    article: int
    section_title: str
    page: int
    text: str


@dataclass
class EmbeddedChunk:
    chunk: Chunk
    embedding: np.ndarray