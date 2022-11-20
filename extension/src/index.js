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
    if (info.menuItemId == "Concept-Map" && info.selectionText) {
        generateMap(info.selectionText);
        chrome.tabs.create({ url: api });
    }
  })



console.log("================ index.js ended ==================")