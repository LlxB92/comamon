odoo.define('percent_field.basic_fields', function (require) {
    "use strict";
    let field_registry = require('web.field_registry');
    let basic_fields = require('web.basic_fields');
    let FieldFloat = basic_fields.FieldFloat;

    /*
     * extending the default float field
     */
    let B92FieldPercent = FieldFloat.extend({

        // formatType is used to determine which format (and parse) functions
        formatType:'Percent',
        /**
         * to override to indicate which field types are supported by the widget
         *
         * @type Array<String>
         */
        supportedFieldTypes: ['float'],
    });

    // registering percent field
    field_registry
        .add('Percent', B92FieldPercent);
    return {
        B92FieldPercent: B92FieldPercent
    };
});

