import axios from "axios";

const baseURL = "http://127.0.0.1:5001"

const $host = axios.create({
    baseURL
})

export { $host }