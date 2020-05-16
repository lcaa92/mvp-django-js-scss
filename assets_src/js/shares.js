import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css'
var $  = require( 'jquery' );
require( 'datatables.net-bs4' );

$('#tableShares').DataTable( {
    "ajax": {
      "url": ctx.data_url,
      "type": "GET",
    },
    "columns": [
        { "data": "code" },
        { "data": "company" },
        { "data": "price" },
    ]
  })