import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css'
var $  = require( 'jquery' );
require( 'datatables.net-bs4' );

console.log(ctx)
$('#tableUsers').DataTable( {
    "ajax": {
      "url": ctx.data_url,
      "type": "GET",
    },
    "columns": [
        { "data": "id" },
        { "data": "username" },
        { "data": "superuser" },
        { "data": "active" },
    ]
  })