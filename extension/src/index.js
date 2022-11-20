console.log("================ index.js connected ==================")
chrome.runtime.onInstalled.addListener(function() {
// creates a listner that listens for the context menu
  chrome.contextMenus.create({
  // creates the context menu item
      "title": "Create Concept Map",
      "contexts": ["selection"],
      "id": "Concept-Map"
  });
});

import axios from "axios"
const api = "http://127.0.0.1:8000/"

const generateMap = async text => {
  console.log("in generateMap");
  if (text === "") { return }
  try {
      console.log("in the try-catch");
      const response = await axios.post(`${api}`, { text: text });
      // document.getElementById('conceptMap').src += '';
  } catch (error) {}
};

chrome.contextMenus.onClicked.addListener(function(info) {

  // runs the code bellow when the context menu item is clicked
    let text = info.selectionText
    if (info.menuItemId == "Concept-Map" && text) {
        // generateMap(info.selectionText);
        let id = Math.random().toString(36).slice(2)
        chrome.tabs.create({ url: `${api + id}?text=${text}` });
    }
  })



console.log("================ index.js ended ==================")