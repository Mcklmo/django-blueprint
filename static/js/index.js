
function load() {

    // get user input for table
    addListeners()

}

function addListeners() {
    enterKey()


}
function enterKey() {
    // add keybord listener for enter key
    document.addEventListener('keydown', e => {
        if (e.keyCode === 13) {
            // hit connect button
            connect()
        }
    })
}


async function connect() {
    // get user input for db connection
    let db_host = document.getElementById("db_host").value;
    let db_user = document.getElementById("db_user").value;
    let db_pass = document.getElementById("db_pass").value;
    let db_name = document.getElementById("db_name").value;
    // input validation
    if (db_host === "" || db_user === "" || db_name === "") {
        alert("Please fill out all fields");
        return;
    }

    // connect to db at server
    let res = await fetch(`/connect`, {
        'method': 'POST',
        'headers': { 'Content-Type': 'application/json' },
        'body': JSON.stringify({
            'host': db_host,
            'user': db_user,
            'password': db_pass,
            'database': db_name
        })
    })
    let data = await res.json();
    if (data.success) {
        // if successful, load table/input endpoint
        window.location.href = "/calculate";

    }
    else {
        alert(data.error)

    }

}