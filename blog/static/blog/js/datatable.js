const dataTableOptions ={
    columnDefs:[
        {orderable:false, target:[3,4]},
        {searchable: false, targets:[3,4]}
    ],
};



$(document).ready(function () {
    $('#tableInfo').DataTable({pageLength : 7});
});