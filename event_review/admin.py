from django.contrib import admin
from django import forms
from django.utils.html import format_html, mark_safe

from event_store.models import Event
from huerta.filters import CollapsedListFilter

def event_list_display(obj):
    return format_html("""
        <div class="row">
            <div class="col-md-6">
                <h5>{title}</h5>
                {private}
                <div><b>Host:</b> {host}</div>
                <div><b>Venue:</b> {venue}</div>
                <div><b>Description</b> {description}</div>
            </div>
            <div class="col-md-6">
                <div><b>Review Status:</b> {review_status}</div>
                <div><b>Prep Status:</b> {prep_status}</div>
                <div><b>Active Status:</b> {active_status}</div>
                <div><b>Notes:</b> {notes}</div>
            </div>
        </div>
        """,
        title=obj.title,
        venue=obj.venue,
        private=mark_safe('<div class="alert alert-danger">Private</div>') if obj.is_private else '',
        host=obj.organization_host,
        review_status=obj.organization_status_review,
        prep_status=obj.organization_status_prep,
        active_status=obj.status,
        notes=mark_safe('<textarea rows="5" class="form-control" readonly>%s</textarea>' % obj.notes)
            if obj.notes else None,
        description = mark_safe('<textarea rows="5" class="form-control" readonly>%s</textarea>' % obj.public_description)
            if obj.public_description else None)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    change_list_template = "admin/change_list_filters_top.html"
    filters_collapsable = True
    filters_require_submit = True
    disable_list_headers = True
    list_striped = True
    list_display = (event_list_display,)
    list_filter = (('organization_campaign', CollapsedListFilter),
                   ('organization_status_review', CollapsedListFilter),
                   ('organization_status_prep', CollapsedListFilter),
                   ('state', CollapsedListFilter),
                   ('is_private', CollapsedListFilter),
                   ('starts_at', CollapsedListFilter),
                   ('ends_at', CollapsedListFilter),
                   ('attendee_count', CollapsedListFilter),
                   ('status', CollapsedListFilter),
                   ('host_is_confirmed', CollapsedListFilter))
    list_display_links = None

    def get_actions(self, request):
        actions = super(EventAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
