import axios from "axios";
const api = "http://127.0.0.1:8000";

const form = document.querySelector(".form-data");
const submittedText = document.querySelector(".text");

let result = "";

const generateMap = async text => {
    try {
      const response = await axios.get(`${api}/${text}`);
      console.log("succeeded")
    } catch (error) {
        console.log("failed");
    }
};

const handleSubmit = async e => {
    e.preventDefault();
    generateMap(submittedText.value);
    console.log("submitted");
};

form.addEventListener("submit", e => handleSubmit(e));