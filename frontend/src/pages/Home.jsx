import { useState } from "react";

import Layout from "../components/layout/Layout";
import ChatWindow from "../components/chat/ChatWindow";
import ChatInput from "../components/chat/ChatInput";

import api from "../services/api";

export default function Home() {
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleSend = async (message) => {
        // Immediately display the user's message
        setMessages((prev) => [
            ...prev,
            {
                role: "user",
                content: message,
            },
        ]);

        setLoading(true);

        try {
            const response = await api.post("/ask", {
                question: message,
            });

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: response.data.answer,
                },
            ]);
        } catch (error) {
            console.error(error);

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: "Unable to contact the server. Please try again.",
                },
            ]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout>
            <div className="flex h-full flex-col">
                {messages.length === 0 ? (
                    <div className="flex flex-1 items-center justify-center">
                        <h2 className="text-4xl font-bold text-slate-500">
                            Ask me anything about Nigerian Law
                        </h2>
                    </div>
                ) : (
                    <ChatWindow
                        messages={messages}
                        loading={loading}
                    />
                )}

                <ChatInput onSend={handleSend} />
            </div>
        </Layout>
    );
}