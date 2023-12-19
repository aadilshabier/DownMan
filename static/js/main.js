"use strict";

const createListItem = (item) => {
	const newItem = document.createElement("li");
	newItem.setAttribute("class", "list-group-item");
	const newContent = document.createTextNode(item.url);
	newItem.append(newContent);
	return newItem;
}

// TODO: Use Web Worker API
const populateDownloadList = () => {
	const downloadList = document.getElementById("downloadList");
	const newChildren = Array();

	fetch("/status", {"method":"GET"})
		.then((response) => {
			if (!response.ok) {
				throw new Error(`HTTP error! Status: ${response.status}`);
			}

			return response.json();
		})
		.then((array) => {
			for (const item of array) {
				const newItem = createListItem(item);
				newChildren.push(newItem);
			}
		})
		.then(() => {
			downloadList.replaceChildren(...newChildren);
		});
}

const addItems = () => {
	const url = document.getElementById("inputURL").value;
	const name = document.getElementById("inputName").value;

	let body = [{"url":url, "name":name, "completed": false}];

	fetch("/add", {
		"method": "PUT",
		"headers": {
			"Content-Type": "application/json",
		},
		"body": JSON.stringify(body),
	});
}

// run once every second
setInterval(populateDownloadList, 1000);
