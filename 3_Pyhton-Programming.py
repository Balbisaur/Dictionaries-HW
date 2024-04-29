service_tickets = {
    "Ticket001": {"Customer": "Gerardo", "Issue": "No Connection", "Status": "open"},
    "Ticket002": {"Customer": "Myron", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id in service_tickets:
        print("ticket already in-use") # checking to see if a ticket already exists in my service tickets, if it doesnt find a ticket. A new ticket will be opened
    else:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print("new ticket has opened.")

def update_status(ticket_id, new_status):
    if ticket_id in service_tickets: #checking to see if a ticket exists in my service tickets, if it finds a ticket, it will update the status from open to closed
        service_tickets[ticket_id]["Status", "closed"] = new_status
        print(f"Status of ticket {ticket_id} updated to {new_status}.")
    else:
        print("ticket not available")

def display_tickets(status=None):
    if status:
        filtered_tickets = {ticket_id: ticket_info for ticket_id, ticket_info in service_tickets.items() if ticket_info["Status"] == status}
        if filtered_tickets:
            print(f"Tickets with status '{status}':")
            for ticket_id, ticket_info in filtered_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")
        else:
            print(f"No tickets found with the status '{status}'.")
    else:
        print("All tickets: ")
        for ticket_id, ticket_info in service_tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")


open_ticket("Ticket003", "Daniela", "Product yet to arrive") 
display_tickets()

update_status("Ticket001", "closed")
display_tickets()

display_tickets("open")


