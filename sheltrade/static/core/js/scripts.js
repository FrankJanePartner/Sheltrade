document.querySelector('.crypto-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents the form from submitting and reloading the page
    // Add any additional code to handle form submission here
  });
  

// JavaScript to update the transaction summary
document.querySelectorAll('select, input').forEach(element => {
    element.addEventListener('change', updateSummary);
});

function updateSummary() {
    document.getElementById('summary-network').textContent = document.getElementById('network').value || '-';
    document.getElementById('summary-phone-number').textContent = document.getElementById('phone-number').value || '-';
    const amount = document.getElementById('amount').value|| '-';
    const currency = document.getElementById('currency').value;
    document.getElementById('summary-amount').textContent = amount ? `${amount} ${currency.toUpperCase()}` : '-';
    document.getElementById('summary-service-provider').textContent = document.getElementById('service-provider').value || '-';
    document.getElementById('summary-account-id').textContent = document.getElementById('account-id').value || '-';
}

  
document.addEventListener('DOMContentLoaded', function() {
    const serviceProviderSelect = document.getElementById('service-provider');
    const planSelectionDiv = document.getElementById('plan-selection');
    const servicePlanSelect = document.getElementById('service-plan');
    const accountIdInput = document.getElementById('account-id');
    const summaryNetwork = document.getElementById('summary-network');
    const summaryPlan = document.getElementById('summary-plan');
    const summaryAccountId = document.getElementById('summary-account-id');

    const plans = {
        dstv: ['DStv Premium', 'DStv Compact Plus', 'DStv Compact', 'DStv Family', 'DStv Access'],
        gotv: ['GOtv Max', 'GOtv Jolli', 'GOtv Jinja', 'GOtv Lite'],
        startimes: ['Nova', 'Basic', 'Smart', 'Classic', 'Super'],
        phcn: ['Prepaid meter recharge', 'Postpaid bill payment']
    };

    

    serviceProviderSelect.addEventListener('change', function() {
        const selectedProvider = this.value;
        
        if (selectedProvider) {
            servicePlanSelect.innerHTML = '<option value="">Select Plan</option>';
            
            plans[selectedProvider].forEach(plan => {
                const option = document.createElement('option');
                option.value = plan.toLowerCase().replace(/\s+/g, '-');
                option.textContent = plan;
                servicePlanSelect.appendChild(option);
            });
            
            planSelectionDiv.style.display = 'block';
        } else {
            planSelectionDiv.style.display = 'none';
        }
        updateSummary();
    });

    servicePlanSelect.addEventListener('change', updateSummary);
    accountIdInput.addEventListener('input', updateSummary);

    // Initial summary update
    updateSummary();
});

