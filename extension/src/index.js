import axios from "axios";
const api = "http://127.0.0.1:8000/";

const form = document.querySelector(".form-data");
const submittedText = document.querySelector(".text");

const generateMap = async text => {
    try {
      const response = await axios.post(`${api}`, { text : text });
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
