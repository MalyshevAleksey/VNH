import React, { useState } from 'react';
import UserSelect from './comps/UserSelect';
import './styles/app.css'
import Chat from './comps/Chat';

function App() {
  const [users, setUsers] = useState([]) // список пользователей
  const [selected, setSelected] = useState("Имя пользователя")
  const [messages, setMessaged] = useState([])

  const ws = new WebSocket("ws://localhost:8765");

  const sendOnServer = (message) => {
    ws.onopen = function(e) {
      console.log("Отправляем данные на сервер");
      ws.send(`site 218185090 ${message}`);
      console.log("Данные отправлены на сервер");
    }
  }

  ws.onmessage = function(message) {
    console.log(message)
  }

  ws.onerror = function(error) {
    alert(`[error] Не удалось соединиться`);
  };


  const addUser = () => {
    // добавление пользователя по клику на плюсик
    setUsers([...users, { username: "Имя пользователя_" + (users.length + 1).toString() }])
  }

  const addMessages = () => {
    // отправление сообщения
    let getMassage = document.getElementById("massenger").value
    if(getMassage !== "") {
      setMessaged([...messages, { message: getMassage, type: true}])
      document.getElementById("massenger").value = ""
    }
  }

  const getMessages = () => {
    // получение сообщения
    let getMassage = document.getElementById("massenger").value
    if(getMassage !== "") {
      setMessaged([...messages, { message: getMassage, type: false}])
      document.getElementById("massenger").value = ""
    }
  }

  const selectUser = (event) => {
    // выбор чата
    let e = event.target
    switch (e.tagName) {
      case "DIV":
        setSelected(event.target.children[1].innerHTML)
        break
      case "H2":
        setSelected(event.target.innerHTML)
        break;
      case "P":
        setSelected(event.target.parentElement.children[1].innerHTML)
    }
  }

  return (
    <div className="wrapper">
      <UserSelect users={users} add={addUser} select={selectUser} />
      <Chat selected={selected} messages={messages} add={addMessages} get={getMessages} sendOnServer={sendOnServer}/>
    </div>
  );
}

export default App;
