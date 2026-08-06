import ReactMarkdown from "react-markdown";

export default function ChatMessage({ role, content }) {
    const isUser = role === "user";

    return (
        <div
            className={`flex ${
                isUser ? "justify-end" : "justify-start"
            }`}
        >
            <div
                className={`max-w-3xl rounded-xl px-5 py-4 ${
                    isUser
                        ? "bg-blue-600 text-white"
                        : "bg-slate-800 text-slate-100"
                }`}
            >
                <ReactMarkdown>{content}</ReactMarkdown>
            </div>
        </div>
    );
}