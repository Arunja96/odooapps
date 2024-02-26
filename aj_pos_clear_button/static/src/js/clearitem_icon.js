odoo.define('aj_pos_clear_button.RemoveItem', function(require){
'use strict';

    const {userState, userRef, onPatched } = owl;
    const { useListener } = require("@web/core/utils/hooks");
    const { onChangeOrder } = require("point_of_sale.custom_hooks");
    const PosComponent = require("point_of_sale.PosComponent");
    const Registries = require("point_of_sale.Registries");
    const Orderline = require("point_of_sale.Orderline");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const OrderWidget = require("point_of_sale.OrderWidget");


    const OrderLineRemove = (Orderline) =>
    class extends Orderline {
    async clear_button_fun() {
        this.trigger('numpad-click-input', { key: 'Backspace' });
        this.trigger('numpad-click-input', { key: 'Backspace' });

    }};
    Registries.Component.extend(Orderline, OrderLineRemove);
    return OrderWidget;

});