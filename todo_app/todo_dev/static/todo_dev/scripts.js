function changeText() {
    var button = document.getElementById('clickButton');
    button.innerText = "HEY CUTIE";
    var input = document.getElementById('task-input');
    var ul = document.getElementById("tasks");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(input.value));
    ul.appendChild(li);
    input.value = ""
}

