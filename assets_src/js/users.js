import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css'
var $  = require( 'jquery' );
require( 'datatables.net-bs4' );

var table_id = '#'.concat(ctx.table_id)
$(table_id).DataTable( {
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