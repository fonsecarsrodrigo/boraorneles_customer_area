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
  const Customer_delete_cell = row.insertCell(7);
  const Customer_delete_btn = document.createElement('img');
  Customer_delete_btn.src = 'images/trash-can.png';
  Customer_delete_btn.alt = 'Delete';
  Customer_delete_btn.className = 'icon';
  Customer_delete_btn.addEventListener('click', () => {
    deleteTravelPlan(travel_plan_id);
    deleteCustomer(customer_key);
  });
  Customer_delete_cell.appendChild(Customer_delete_btn);
};

async function insertTravelPlanRow ({ travel_plan_key, customer_id, origin, destination, start_date, end_date, travel_purpose }) {
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
    row.insertCell(0).textContent = travel_plan_key ?? '';
    row.insertCell(1).textContent = customer_id ?? '';
    row.insertCell(2).textContent = full_name ?? '';
    row.insertCell(3).textContent = origin ?? '';
    row.insertCell(4).textContent = destination ?? '';
    row.insertCell(5).textContent = start_date
    row.insertCell(6).textContent = end_date
    row.insertCell(7).textContent = travel_purpose ?? '';
    const TP_delete_cell = row.insertCell(8);
    const TP_delete_btn = document.createElement('img');
    TP_delete_btn.src = 'images/trash-can.png';
    TP_delete_btn.alt = 'Delete';
    TP_delete_btn.className = 'icon';
    TP_delete_btn.addEventListener('click', () => deleteTravelPlan(travel_plan_key));
    TP_delete_cell.appendChild(TP_delete_btn);
  } catch (error) {
    console.error('Error fetching customer name:', error);
  }
};

const deleteTravelPlan = (travel_plan_key) => {
  const url = `${API_BASE_URL}/delete_travel_plan?travel_plan_key=${travel_plan_key}`;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      console.info('ROUTE: /delete_travel_plan response ok');
      return response.json();
    })
    .then((data) => {
      console.info('ROUTE: /delete_travel_plan data received', data);
      alert('Travel plan deleted successfully.');
      location.reload();
    })
    .catch((error) => {
      console.error('ROUTE: /delete_travel_plan failed with error:', error);
    });
}

const deleteCustomer = (customer_key) => {
  const url = `${API_BASE_URL}/delete_customer?customer_key=${customer_key}`;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }
      console.info('ROUTE: /delete_customer response ok');
      return response.json();
    })
    .then((data) => {
      console.info('ROUTE: /delete_customer data received', data);
      alert('Customer deleted successfully.');
      location.reload();
    })
    .catch((error) => {
      console.error('ROUTE: /delete_customer failed with error:', error);
    });
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

const addTravelPlan = (event) => {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);
  const payload = {
    customer_id: formData.get('customer_id'),
    origin: formData.get('origin'),
    destination: formData.get('destination'),
    start_date: formData.get('start_date').toString(),
    end_date: formData.get('end_date').toString(),
    travel_purpose: formData.get('travel_purpose') || '',
  };
    const url = `${API_BASE_URL}/add_travel_plan`;
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
      console.info('ROUTE: add_travel_plan response ok', data)
    })
    .catch((error) => {
      console.error('ROUTE: add_travel_plan failed with error:', error);
    });
};

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('customerForm');
  if (form) {
    form.addEventListener('submit', addCustomer);
  }

  TP_form = document.getElementById('travelPlanForm')
  if (TP_form) {
    TP_form.addEventListener('submit', addTravelPlan);
  }

  showCustomers();
  showTravelPlans();

});
