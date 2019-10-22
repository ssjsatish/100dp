var randomNumber = Date.now();

var mainSkipLink = document.getElementById("skiplink");

var rootDiv = document.createElement("div");
rootDiv.id = "root";

var appDiv = document.createElement("div");
appDiv.className = "App";

var botSkipLink = document.createElement("a");
botSkipLink.setAttribute('href', '#chatbot');
botSkipLink.setAttribute('aria-label', 'Skip to chat bot.');
botSkipLink.className = "skipnav";
var botSkipLinkText = document.createTextNode("Skip to MediClaire Chatbot");
botSkipLink.appendChild(botSkipLinkText);

var cssScript = document.createElement('link');
cssScript.setAttribute('rel', 'stylesheet');
cssScript.setAttribute('href', 'https://nonprod.va.optum.com/mmc-ui-dev/static/css/main.css?v=' + randomNumber);


var bundleScript = document.createElement('script');
bundleScript.setAttribute('src', 'https://nonprod.va.optum.com/mmc-ui-dev/static/js/bundle.js?v=' + randomNumber);

var mainScript = document.createElement('script');
mainScript.setAttribute('src', 'https://nonprod.va.optum.com/mmc-ui-dev/static/js/main.js?v=' + randomNumber);

document.head.insertBefore(cssScript, document.head.firstChild);
document.body.insertBefore(botSkipLink, mainSkipLink.nextSibling);
document.body.appendChild(bundleScript);
document.body.appendChild(mainScript);
document.body.insertBefore(rootDiv, botSkipLink.nextSibling);
rootDiv.appendChild(appDiv);

