openerp.pos_driver = function(instance, local) {

    var _t = instance.web._t,
    _lt = instance.web._lt;
    var QWeb = instance.web.qweb;
    var pos = instance.point_of_sale.PosModel;

    instance.point_of_sale.HeaderButtonWidget.include({
        start: function(){
            var driver_id;
            var self = this;
            var res_users = new instance.web.Model("res.users");
            res_users.query()
            .filter([['is_delivery', '=', true]])
            .all().then(function (users) {
                $.each(users,function(index, driver){
                    $(".ul-drivers").append('<li id="' + driver.id + '"><img src="data:image/png;base64,'+ driver.image_small +'" /><h3>' + driver.display_name  + '</h3></li>');
                });
                $(".ul-drivers li").click(function(){
                    $(".ul-drivers li").css("background", "white");
                    $(".ul-drivers li").css("opacity","1");
                    $(this).css("background", "rgb(96, 228, 233)");
                    $(this).css("opacity","0.85");
                    driver_id = parseInt($(this).attr('id'));
                    self.pos.get('selectedOrder').set_delivery(driver_id);
                    $(".driver-dialog").hide();
                });
            });
            this._super();
            $(".pos-rightheader").append(QWeb.render('pos_driver'));
            $('body').append(QWeb.render('driver-dialog'));
            
            $(".driver-button").click(function(){
                $(".driver-dialog").show();
            });
            $(".dialog-popup-driver-overlay").click(function(){
                $(".driver-dialog").hide();
            });
        },
    });

    instance.point_of_sale.Order = instance.point_of_sale.Order.extend({
        set_delivery: function(delivery_id){
            this.set('pos_driver', delivery_id);
        },
        get_delivery: function(){
            return this.get('pos_driver');
        },

        export_as_JSON: function() {
            var orderLines, paymentLines;
            orderLines = [];
            (this.get('orderLines')).each(_.bind( function(item) {
                return orderLines.push([0, 0, item.export_as_JSON()]);
            }, this));
            paymentLines = [];
            (this.get('paymentLines')).each(_.bind( function(item) {
                return paymentLines.push([0, 0, item.export_as_JSON()]);
            }, this));
            return {
                name: this.getName(),
                amount_paid: this.getPaidTotal(),
                amount_total: this.getTotalTaxIncluded(),
                amount_tax: this.getTax(),
                amount_return: this.getChange(),
                lines: orderLines,
                statement_ids: paymentLines,
                pos_session_id: this.pos.pos_session.id,
                partner_id: this.get_client() ? this.get_client().id : false,
                user_id: this.pos.cashier ? this.pos.cashier.id : this.pos.user.id,
                uid: this.uid,
                sequence_number: this.sequence_number,
                pos_delivery: this.get_delivery() || false,
            };
        },
    });
    
}