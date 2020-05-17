import 'datatables.net-bs4/css/dataTables.bootstrap4.min.css'
var $  = require( 'jquery' );
require( 'datatables.net-bs4' );

let tablesElements = $('table')
tablesElements.each(function( key, tableEl ) {
  if (tableEl.dataset.configKey === undefined){
    console.log('config key not found');
    return
  }

  let config = ctx.datatable[tableEl.dataset.configKey]
  if (config === undefined){
    console.log('config not found');
    return
  }

  let columnsDefs = []
  let columnsValue = []

  if (config.columnsTitle){
    config.columnsTitle.forEach(function(value, key){
      columnsDefs.push({
        "title": value, "targets": key
      })
    })
  }

  if (config.columnsValue){
    config.columnsValue.forEach(function(value){
      columnsValue.push({
        "data": value
      })
    })
  }

  $(tableEl).DataTable( {
    "ajax": {
      "url": config.data_url,
      "type": "GET",
    },
    "columnDefs":  columnsDefs,
    "columns": columnsValue
  })
});

