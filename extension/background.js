

console.log("================ Background.js connected ==================")
chrome.runtime.onInstalled.addListener(function() {
// creates a listner that listens for the context menu
  chrome.contextMenus.create({
  // creates the context menu item
      "title": "Create Concept Map",
      "contexts": ["selection"],
      "id": "Concept-Map"
  });
});

chrome.contextMenus.onClicked.addListener(function(info) {

  // runs the code bellow when the context menu item is clicked
    if (info.menuItemId == "Concept-Map" && info.selectionText){
        chrome.tabs.create({ url: "http://127.0.0.1:5000" });
    }
  })



console.log("================ Background.js ended ==================")