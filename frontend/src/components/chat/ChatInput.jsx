import { useState } from "react";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { SendHorizontal } from "lucide-react";

export default function ChatInput({ onSend }) {
    const [message, setMessage] = useState("");

    const handleSubmit = () => {
        if (!message.trim()) return;

        onSend(message);
        setMessage("");
    };

    return (
        <div className="border-t border-slate-800 bg-slate-950 p-4">
            <div className="flex gap-3">
                <Textarea
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Ask a question about Nigerian law..."
                    className="min-h-[60px] resize-none"
                    onKeyDown={(e) => {
                        if (e.key === "Enter" && !e.shiftKey) {
                            e.preventDefault();
                            handleSubmit();
                        }
                    }}
                />

                <Button onClick={handleSubmit} size="icon">
                    <SendHorizontal className="h-5 w-5" />
                </Button>
            </div>
        </div>
    );
}