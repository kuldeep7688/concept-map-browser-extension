const url = "localhost:8080/";

chrome.runtime.onInstalled.addListener(function() {
  // creates a listener that listens for the context menu
    chrome.contextMenus.create({
    // creates the context menu item
        "title": "Create Concept Map",
        "contexts": ["selection"],
        "id": "Concept-Map"
    });
});
    
chrome.contextMenus.onClicked.addListener(function(info) {
// runs the code bellow when the context menu item is clicked
  if (info.menuItemId == "Concept-Map" && info.selectionText) {
    request({
        url: url,
        method: 'GET',
        json: JSON.parse(info.selectionText)
      }, function(err, resp, body){
        if(err){
            console.log('Could not create map.');
            console.log(err);
        }
      }
    );
  }
});