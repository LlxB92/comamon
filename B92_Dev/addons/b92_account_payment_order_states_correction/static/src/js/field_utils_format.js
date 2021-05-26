odoo.define('percent_field.field_utils_format', function (require) {
    "use strict";
    let field_utils = require('web.field_utils');
    let percent_char = " %"

    function formatPercent(value) {
        return (value ? value : 0.0 ) + percent_char;
    }

    field_utils['format']['Percent'] = formatPercent;
});

