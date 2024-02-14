
let addActivityToList = document.getElementById("input_area");
let addButton = document.getElementById("add");
let activity = document.getElementById("activities");


function addToList(){
    createList();
    addActivityToList.value = "";
}

function createList(){
    let li = document.createElement("li");
    li.className = "content";
    let checkbox = document.createElement('input');
    let paragraph = document.createElement('p');
    let deleteElement = document.createElement('button');

    let divCheckbox = document.createElement('div');
    let divActivity = document.createElement('div')
    let divDelete = document.createElement('div');

    divCheckbox.className = "checkbox";
    divCheckbox.classList.add("row");
    divActivity.className = "activity";
    divActivity.classList.add("row");
    divDelete.className = "delete_box";
    divDelete.classList.add("row");


    checkbox.type = "checkbox";
    checkbox.className = "galochka";
    checkbox.classList.add("row");
    divCheckbox.appendChild(checkbox);
    li.appendChild(divCheckbox);

    paragraph.textContent = addActivityToList.value;
    paragraph.className = "activity-info";
    paragraph.classList.add("row");
    divActivity.appendChild(paragraph);
    li.appendChild(divActivity);

    deleteElement.textContent = "Delete";
    deleteElement.className = "delete";
    deleteElement.classList.add("row");
    deleteElement.addEventListener("click", () => {
        activity.removeChild(li);
    })
    divDelete.appendChild(deleteElement);
    li.appendChild(divDelete);

    checkbox.addEventListener("change", () => {
        if (checkbox.checked)
            paragraph.classList.add('line');
        else
            paragraph.classList.remove('line');

    })
    activity.appendChild(li);

}