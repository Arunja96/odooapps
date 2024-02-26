odoo.define('aj_pos_clear_button.ClearButton', function(require){
'use strict';

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    const { useListener } = require('@web/core/utils/hooks');


    class ClearButton extends PosComponent {

    setup(){
        super.setup();
        useListener("click", this.clearAllButtonClick)
    }
    async clearAllButtonClick(){

        const { confirmed }= await this.showPopup('ConfirmPopup',{
            title: "CONFIRM",
            body:"Are you sure?",
            confirmText: "Yes",
            cancelText: "No"
        });
        if (confirmed){
            var current_order = this.env.pos.get_order();
            current_order.orderlines.filter(line=> line.get_product()).forEach(single_line=> current_order.remove_orderline(single_line));
        }

    }

    }

    ClearButton.template = "ClearButton"
    ProductScreen.addControlButton({
        component: ClearButton,
        position: ["after",'RefundButton'],
    })
    Registries.Component.add(ClearButton);

    return ClearButton;
})