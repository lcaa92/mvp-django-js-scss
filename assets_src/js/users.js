import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css'
var $  = require( 'jquery' );
require( 'datatables.net-bs4' );

$('#tableUsers').DataTable( {
    "ajax": {
      "url": "http://localhost:8000/dashboard/data/administration/users",
      "type": "GET",
    },
    "columns": [
        { "data": "id" },
        { "data": "username" },
        { "data": "superuser" },
        { "data": "active" },
    ]
  })