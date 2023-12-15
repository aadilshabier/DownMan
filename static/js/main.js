"use strict";

const createListItem = (item) => {
	const newItem = document.createElement("div");
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
				// console.log(item.url);
				const newItem = createListItem(item);
				newChildren.push(newItem);
			}
		})
		.then(() => {
			console.log(newChildren);
			downloadList.replaceChildren(...newChildren);
		});
}
