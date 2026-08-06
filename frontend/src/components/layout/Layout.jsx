import Header from "./Header";

export default function Layout({ children }) {
    return (
        <div className="flex h-screen flex-col bg-slate-950 text-white">
            <Header />

            <main className="flex-1 overflow-hidden">
                {children}
            </main>
        </div>
    );
}