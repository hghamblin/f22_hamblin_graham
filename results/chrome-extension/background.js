function changeTitle() {
    alert("u r mr.gay");
}
  
chrome.action.onClicked.addListener((tab) => {
    if(!tab.url.includes("chrome://")) {
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: changeTitle
        });
    }
});