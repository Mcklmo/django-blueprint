function load(){
    addListeners()
    getUserTables()
}

function addListeners(){
    
    
}

async function getUserTables(){
    let res = await fetch(`/tables/all`)
    let data = await res.json()
    console.log(data)
    if(data.success){
        // add tables as options to select tab
        tables=data.tables
        for(let i=0;i<tables.length;i++){
            let option = document.createElement("option")
            option.value=tables[i]
            option.innerHTML=tables[i]
            document.getElementById("table").appendChild(option)
        }
    }
    else {
        alert(data.error)
    }
}