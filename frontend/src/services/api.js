import axios from "axios";

const api = axios.create({
    baseURL: "https://nigerian-law-expert-backend.onrender.com",
});

export default api;