## Release 1 Rollback Plan

### Objective

Restore the pre-release digital banking experience if the October 5 production activation creates a material customer, security, compliance, or operational problem.

### Rollback Triggers

Rollback may be initiated when:

- Credit Sense causes disruption to normal OLB or mobile banking.
- SSO, enrollment, entitlements, or customer-data mapping fails materially.
- One customer can access another customer’s information.
- A security, privacy, consent, or disclosure issue is identified.
- Credit Sense is broadly unavailable without an acceptable workaround.
- Production monitoring cannot confirm that the service is operating safely.
- The Digital Lead, Technology Lead, Product Lead, or vendor recommends withdrawal.

Security, privacy, or cross-customer data issues require immediate disablement.

### Rollback Actions

1. **Stop additional changes.** Technology freezes the release and opens an incident record.

2. **Disable customer access.** Technology and Fiserv disable the Credit Sense navigation, entitlement, SSO connection, or feature configuration.

3. **Remove launch entry points.** Digital removes or hides Credit Sense links from OLB and mobile banking.

4. **Pause communications.** Marketing stops scheduled emails, banners, promotions, website content, and employee announcements that have not been released.

5. **Secure the vendor configuration.** SavvyMoney leaves the production tenant intact but prevents new customer access. Configuration and customer records are not deleted during the incident.

6. **Restore the previous digital configuration.** Technology restores the approved pre-release navigation, entitlement, and authentication settings.

7. **Validate the rollback.** Technology and Product confirm:

   - Normal OLB and mobile banking remain available.
   - Credit Sense links no longer appear.
   - New SSO sessions cannot be initiated.
   - No incorrect customer access is possible.
   - Monitoring has returned to normal levels.
   - Support teams have the correct customer guidance.

8. **Communicate the outcome.** Digital provides an internal status update. Customer Support uses the approved incident script. External communication is issued only when customers were affected or previously notified.

### Team Responsibilities

- **Digital:** Coordinates the rollback, maintains the incident timeline, and communicates status.
- **Product:** Confirms the customer experience is safely withdrawn and determines business impact.
- **Marketing:** Pauses or removes launch communications and promotions.
- **Technology:** Disables access, restores configuration, validates OLB stability, and preserves logs.
- **Vendor:** Fiserv and SavvyMoney complete vendor-side disablement and confirm system status.
- **Data and Analytics:** Monitors errors, access attempts, enrollment activity, and customer impact.
- **QA:** Performs functional confirmation of the restored configuration if requested.
- **Customer Support:** Activates the incident script, records customer contacts, and escalates patterns.
- **Corporate Training:** Distributes updated employee guidance if operating procedures change.

### Target Timing

- Incident identified and owners engaged: within 15 minutes
- Rollback decision: within 30 minutes
- Customer access disabled: within 60 minutes
- Restoration validation and internal communication: within 90 minutes

These times must be confirmed with Fiserv and SavvyMoney by Friday, October 2.

### Return-to-Service Requirements

Credit Sense cannot be reactivated until the cause is understood, corrections pass functional QA and UAT as applicable, security and compliance concerns are resolved, and a new Go or No Go approval is recorded.