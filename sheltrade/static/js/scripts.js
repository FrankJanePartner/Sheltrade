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
    document.getElementById('summary-bundle-type').textContent = document.getElementById('bundle-type').value || '-';
    document.getElementById('summary-phone-number').textContent = document.getElementById('phone-number').value || '-';
    const amount = document.getElementById('amount').value|| '-';
    const currency = document.getElementById('currency').value;
    document.getElementById('summary-amount').textContent = amount ? `${amount} ${currency.toUpperCase()}` : '-';
    document.getElementById('summary-service-provider').textContent = document.getElementById('service-provider').value || '-';
    document.getElementById('summary-account-id').textContent = document.getElementById('account-id').value || '-';
}

// JavaScript to handle tab switching
function openTab(evt, tabName) {
    // Hide all tab contents
    const tabContents = document.getElementsByClassName('tab-content');
    for (let i = 0; i < tabContents.length; i++) {
      tabContents[i].style.display = 'none';
    }
  
    // Remove "active" class from all buttons
    const tabButtons = document.getElementsByClassName('tab-button');
    for (let i = 0; i < tabButtons.length; i++) {
      tabButtons[i].className = tabButtons[i].className.replace(' active', '');
    }
  
    // Show the clicked tab content and add "active" class to the clicked button
    document.getElementById(tabName).style.display = 'block';
    evt.currentTarget.className += ' active';
  }
  
  // Show the first tab by default when the page loads
  document.addEventListener('DOMContentLoaded', function() {
    document.getElementsByClassName('tab-button')[0].click();
  });
  
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

    function updateSummary() {
        const selectedProvider = serviceProviderSelect.value;
        const selectedPlan = servicePlanSelect.value;
        const accountId = accountIdInput.value;

        summaryNetwork.textContent = selectedProvider ? selectedProvider.toUpperCase() : '-';
        summaryPlan.textContent = selectedPlan ? selectedPlan.replace(/-/g, ' ').toUpperCase() : '-';
        summaryAccountId.textContent = accountId || '-';
    }

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