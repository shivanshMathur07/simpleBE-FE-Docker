import React, { useState } from 'react';

const Form = ({ onAdd }) => {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name || !age) return;
    const res = await fetch('http://localhost:5000/records', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-api-key' : '123456' },
      body: JSON.stringify({ name, age }),
    });
    if (res.ok) {
      const data = await res.json();
      onAdd(data);
      setName('');
      setAge('');
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{
        display: 'flex',
        flexDirection: 'column',
        gap: '1rem',
        alignItems: 'center',
        justifyContent: 'center',
        minHeight: '200px',
        background: '#f9f9f9',
        padding: '2rem',
        borderRadius: '8px',
        boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
      }}
    >
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={e => setName(e.target.value)}
        style={{ padding: '0.5rem', width: '200px' }}
      />
      <input
        type="number"
        placeholder="Age"
        value={age}
        onChange={e => setAge(e.target.value)}
        style={{ padding: '0.5rem', width: '200px' }}
      />
      <button type="submit" style={{ padding: '0.5rem 1rem' }}>Add</button>
    </form>
  );
};

export default Form;