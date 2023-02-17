let dataTable;
let dataTableInitialized=false;

const dataTableOptions ={
    columnDefs:[
        {className: "centered", targets: [0, 1, 2, 3, 4]},
        {orderable: false, targets: [3, 4]},
        {searchable: false, targets:[0, 1, 2]}
    ]
};



const initDataTable=async()=>{
    if(dataTableInitialized){
        dataTable.destroy();
    }
    await listInfos();

    dataInfos=$('#tableInfo').DataTable({dataTableOptions});
    
    dataTableInitialized=true;
};

const listInfos = async()=>{
    try{
        const response=await fetch('http://127.0.0.1:8000/blog/obtenerinfo');
        const data= await response.json();
        let content=``;
        data.infos.forEach((info, index) => {
            content+=`
                <tr>
                    <td>${info.nombre}</td>
                    <td>${info.numero}</td>
                    <td>${info.date }</td>
                    <td>${info.contactado == true ? "<i class='fa-solid fa-check' style='color: green;'></i>" : "<i class='fa-solid fa-xmark' style='color: red;'></i>" }</td>
                    
                    <td>"<button  type='button' class='btn btn-success'>Contactado ${info.id} <i class='fa fa-check-circle' aria-hidden='true'></i></button>"</td>
                </tr>
            `;
        });
        tableBody.innerHTML = content;
        console.log(data.infos);
    }catch(ex){
        alert(ex);
    }
};

window.addEventListener('load', async()=>{
    await initDataTable();
});