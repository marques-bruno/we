
import React, { Component } from "react";

const addressEntries = [
  {
      "id": 1,
      "first_name": "Bruno",
      "last_name": "Marques",
      "address1": "Skultetyho 32",
      "address2": "appt 2",
      "zip_code": "08001",
      "city": "Presov",
      "country": "SK",
      "mobile_phone": "+421949329753",
      "phone": null,
      "additional_information": "Nothing special",
      "is_primary": false,
      "name": "Skultetyho",
      "user": 9
  },
  {
      "id": 2,
      "first_name": "Adriana",
      "last_name": "Vrablova",
      "address1": "Mlynska 2",
      "address2": null,
      "zip_code": "08001",
      "city": "Presov",
      "country": "SK",
      "mobile_phone": "+421000000000",
      "phone": null,
      "additional_information": null,
      "is_primary": false,
      "name": "Mlynska",
      "user": 9
  },
  {
      "id": 3,
      "first_name": "Miroslav",
      "last_name": "Vrabel",
      "address1": "45",
      "address2": null,
      "zip_code": "08201",
      "city": "Drienovska Nova Ves",
      "country": "SK",
      "mobile_phone": "+421111111111",
      "phone": null,
      "additional_information": null,
      "is_primary": false,
      "name": "Adiee's Parents",
      "user": 9
  },
  {
      "id": 15,
      "first_name": "i",
      "last_name": "h",
      "address1": "g",
      "address2": "f",
      "zip_code": "c",
      "city": "d",
      "country": "EC",
      "mobile_phone": null,
      "phone": null,
      "additional_information": "b",
      "is_primary": true,
      "name": "a2",
      "user": 9
  },
  {
      "id": 16,
      "first_name": "a",
      "last_name": "a",
      "address1": "a",
      "address2": "a",
      "zip_code": "a",
      "city": "a",
      "country": "AF",
      "mobile_phone": null,
      "phone": null,
      "additional_information": "a",
      "is_primary": false,
      "name": "a",
      "user": 13
  },
  {
      "id": 17,
      "first_name": "b",
      "last_name": "b",
      "address1": "b",
      "address2": "b",
      "zip_code": "b",
      "city": "b",
      "country": "BS",
      "mobile_phone": null,
      "phone": null,
      "additional_information": "b",
      "is_primary": false,
      "name": "b",
      "user": 13
  },
  {
      "id": 18,
      "first_name": "c",
      "last_name": "c",
      "address1": "c",
      "address2": "c",
      "zip_code": null,
      "city": "c",
      "country": "CV",
      "mobile_phone": null,
      "phone": null,
      "additional_information": "c",
      "is_primary": false,
      "name": "c",
      "user": 13
  },
  {
      "id": 19,
      "first_name": "Nyanya",
      "last_name": "Nyanya",
      "address1": "Nyanya",
      "address2": "Nyanya",
      "zip_code": "Nyanya",
      "city": "Nyanya",
      "country": "NA",
      "mobile_phone": null,
      "phone": null,
      "additional_information": "Nyanya",
      "is_primary": true,
      "name": "Nyanya",
      "user": 13
  }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedUser: addressEntries[0].user,
      addressList: addressEntries,
    };
  }

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ selectedUser: status });
    }

    return this.setState({ selectedUser: status });
  };
  





  renderTabList = () => {
    const users = this.state.addressList.map(addr => addr.user);
    const unique_users = users.filter((u, idx) => users.indexOf(u) === idx);

    return unique_users.map((item) => (
        <span
          className={this.state.selectedUser === item ? "nav-link active" : "nav-link"}
          onClick={() => this.displayCompleted(item)}
        >
          User {item}
        </span>
    ));
  };

  renderItems = () => {
    const { selectedUser } = this.state;
    const newItems = this.state.addressList.filter(
      (item) => { console.log(item.user + " === " + selectedUser); return item.user === selectedUser; }
    );

    console.log(newItems)
    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`addr-title mr-2 ${
            this.state.selectedUser ? "user-address" : ""
          }`}
          title={item.address1}
        >
          {item.name}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Address app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                >
                  Add task
                </button>
              </div>
              <div className="nav nav-tabs">
                {this.renderTabList()}
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;





// import React, { Component } from "react";

// const todoItems = [
//   {
//     id: 1,
//     title: "Go to Market",
//     description: "Buy ingredients to prepare dinner",
//     completed: true,
//   },
//   {
//     id: 2,
//     title: "Study",
//     description: "Read Algebra and History textbook for the upcoming test",
//     completed: false,
//   },
//   {
//     id: 3,
//     title: "Sammy's books",
//     description: "Go to library to return Sammy's books",
//     completed: true,
//   },
//   {
//     id: 4,
//     title: "Article",
//     description: "Write article on how to use Django with React",
//     completed: false,
//   },
// ];

// class App extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       viewCompleted: false,
//       todoList: todoItems,
//     };
//   }

//   displayCompleted = (status) => {
//     if (status) {
//       return this.setState({ viewCompleted: true });
//     }

//     return this.setState({ viewCompleted: false });
//   };

//   renderTabList = () => {
//     return (
//       <div className="nav nav-tabs">
//         <span
//           className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
//           onClick={() => this.displayCompleted(true)}
//         >
//           Complete
//         </span>
//         <span
//           className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
//           onClick={() => this.displayCompleted(false)}
//         >
//           Incomplete
//         </span>
//       </div>
//     );
//   };

//   renderItems = () => {
//     const { viewCompleted } = this.state;
//     const newItems = this.state.todoList.filter(
//       (item) => item.completed == viewCompleted
//     );

//     return newItems.map((item) => (
//       <li
//         key={item.id}
//         className="list-group-item d-flex justify-content-between align-items-center"
//       >
//         <span
//           className={`todo-title mr-2 ${
//             this.state.viewCompleted ? "completed-todo" : ""
//           }`}
//           title={item.description}
//         >
//           {item.title}
//         </span>
//         <span>
//           <button
//             className="btn btn-secondary mr-2"
//           >
//             Edit
//           </button>
//           <button
//             className="btn btn-danger"
//           >
//             Delete
//           </button>
//         </span>
//       </li>
//     ));
//   };

//   render() {
//     return (
//       <main className="container">
//         <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
//         <div className="row">
//           <div className="col-md-6 col-sm-10 mx-auto p-0">
//             <div className="card p-3">
//               <div className="mb-4">
//                 <button
//                   className="btn btn-primary"
//                 >
//                   Add task
//                 </button>
//               </div>
//               {this.renderTabList()}
//               <ul className="list-group list-group-flush border-top-0">
//                 {this.renderItems()}
//               </ul>
//             </div>
//           </div>
//         </div>
//       </main>
//     );
//   }
// }

// export default App;







