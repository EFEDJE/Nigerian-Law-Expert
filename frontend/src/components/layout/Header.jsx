import { Scale } from "lucide-react";

export default function Header() {
    return (
        <header className="border-b border-slate-800 bg-slate-950">
            <div className="mx-auto flex h-20 items-center justify-center">
                <div className="flex items-center gap-4">
                    <Scale className="h-10 w-10 text-blue-500" />

                    <div className="text-left">
                        <h1 className="text-3xl font-bold text-white">
                            Nigerian Law Expert
                        </h1>

                        <p className="text-sm text-slate-400">
                            AI-powered legal assistant
                        </p>
                    </div>
                </div>
            </div>
        </header>
    );
}