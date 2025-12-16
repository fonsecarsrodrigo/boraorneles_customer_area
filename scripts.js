const API_BASE_URL = 'http://127.0.0.1:5000';

const insertCustomerRow = ({ customer_key, full_name, social_number, date_of_birth, e_mail, home_adress, travel_plan_id }) => {
  const table = document.getElementById('CustomersTable');
  if (!table) {
    return;
  }
  const row = table.insertRow(-1);
  row.insertCell(0).textContent = customer_key ?? '';
  row.insertCell(1).textContent = full_name ?? '';
  row.insertCell(2).textContent = social_number ?? '';
  row.insertCell(3).textContent = date_of_birth
  row.insertCell(4).textContent = e_mail ?? '';
  row.insertCell(5).textContent = home_adress ?? '';
  row.insertCell(6).textContent = travel_plan_id ?? '';
  const icon  = row.insertCell(7);
  icon.innerHTML = '<img class="icon" src="images/trash-can.png" alt="Delete">'
};

async function insertTravelPlanRow ({ customer_id, destination, start_date }) {
  const table = document.getElementById('TravelPlansTable');
  if (!table) {
    return;
  }

  const baseUrl = `${API_BASE_URL}/get_customer`;
  full_name = '<DEAD_BEEF>';

  const url = new URL(baseUrl);
  url.searchParams.append('customer_key', customer_id);

  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: { Accept: 'application/json' },
    });

    if (!response.ok) throw new Error(`Request failed with status ${response.status}`);

    const data = await response.json();
    if (data.full_name) full_name = String(data.full_name);

    const row = table.insertRow(-1);
    console.log('Inserting travel plan row for customer:', full_name);
    row.insertCell(0).textContent = customer_id ?? '';
    row.insertCell(1).textContent = full_name ?? '';
    row.insertCell(2).textContent = destination ?? '';
    row.insertCell(3).textContent = start_date
    ? new Date(start_date).toLocaleDateString()
    : '';
  } catch (error) {
    console.error('Error fetching customer name:', error);
  }
};

const showCustomers = () => {
  const url = `${API_BASE_URL}/get_customers`;
  fetch(url, { method: 'get' })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      console.info('ROUTE: /get_customers response ok');
      return response.json();
    })
    .then((data) => {
      if (!data.customers) {
        console.info('ROUTE: /get_customers no customers found');
        return;
      }
      console.info('ROUTE: /get_customers data received', data);
      data.customers.forEach(insertCustomerRow);
    })
    .catch((error) => {
      console.error('ROUTE: /get_customers failed with error:', error);
    });
};

const showTravelPlans = () => {
  const url = `${API_BASE_URL}/get_travel_plans`;
  fetch(url, { method: 'get' })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      console.info('ROUTE: /get_travel_plans response ok');
      return response.json();
    })
    .then((data) => {
      if (!data.travel_plans) {
        console.info('ROUTE: /get_travel_plans no travel plans found');
        return;
      }
      console.info('ROUTE: /get_travel_plans data received', data);
      data.travel_plans.forEach(insertTravelPlanRow);
    })
    .catch((error) => {
      console.error('ROUTE: /get_travel_plans failed with error:', error);
    });
};

const addCustomer = (event) => {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);
  const payload = {
    full_name: formData.get('full_name'),
    e_mail: formData.get('e_mail'),
    date_of_birth: formData.get('date_of_birth').toString(),
    home_adress: formData.get('home_adress') || '',
    social_number: formData.get('social_number'),
    travel_plan_id: null,
  };
    const url = `${API_BASE_URL}/add_customer`;
    fetch(url, {
    method: 'post',
    body: formData
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      response.json()
    })
    .then((data) => {
      console.info('ROUTE: add_customer response ok', data)
    })
    .catch((error) => {
      console.error('ROUTE: add_customer failed with error:', error);
    });
};

document.addEventListener('DOMContentLoaded', () => {
  showCustomers();
  showTravelPlans();
  const form = document.getElementById('customerForm');
  if (form) {
    form.addEventListener('submit', addCustomer);
  }
});
