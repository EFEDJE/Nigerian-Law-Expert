import { useEffect, useRef } from "react";
import ChatMessage from "./ChatMessage";

export default function ChatWindow({ messages, loading }) {
    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [messages, loading]);

    return (
        <div className="flex-1 overflow-y-auto px-8 py-6 space-y-6">
            {messages.map((message, index) => (
                <ChatMessage
                    key={index}
                    role={message.role}
                    content={message.content}
                />
            ))}

            {loading && (
                <ChatMessage
                    role="assistant"
                    loading={true}
                />
            )}

            <div ref={bottomRef} />
        </div>
    );
}