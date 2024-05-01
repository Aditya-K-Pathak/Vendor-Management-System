
class ServiceHandler:
    def OrderHandler(order):

        from VendorProfile.models import VendorProfile

        if VendorProfile.objects.filter(vendor_code=order.vendor_code.vendor_code).exists():
            vendor = VendorProfile.objects.get(vendor_code=order.vendor_code.vendor_code)
            if order.po_number not in vendor.new_orders:
                vendor.new_orders.update({
                    order.po_number: order.order_status
                })
                vendor.orders_received += 1
                vendor.save()
        ServiceHandler.VendorHandler()

    def VendorHandler(vendor):

        from Orders.models import Orders

        for po_number in vendor.new_orders:
            if Orders.objects.filter(po_number=po_number).exists():
                order = Orders.objects.get(po_number=po_number)
                if order.order_status == 'Pending' and vendor.new_orders[po_number] == 'Completed':
                    order.order_status = 'Completed'
                    order.save()
                
