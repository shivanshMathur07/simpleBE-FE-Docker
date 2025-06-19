import React, { useState, useEffect } from 'react';
import Form from './components/Form';
import PeopleList from './components/PeopleList';

function App() {

        const [people, setPeople] = useState([]);

        useEffect(() => {
          fetch('http://localhost:5000/records')
            .then(res => res.json())
            .then(data => {
              console.log('Fetched data:', data);
              setPeople(data)
            });
        }, []);

        const handleAdd = (person) => {
          setPeople(prev => [...prev, person]);
        };

        const handleDelete = async (id) => {
          const res = await fetch(`http://localhost:5000/records/${id}`, { 
            method: 'DELETE',
            headers: { 'x-api-key': '123456' }
        });
          if (res.ok) {
            setPeople(prev => prev.filter(p => p.id !== id));
          }
        };

        return (
          <div style={{
            minHeight: '100vh',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center'
          }}>
            <Form onAdd={handleAdd} />
            <PeopleList people={people} onDelete={handleDelete} />
          </div>
        );
      }

export default App;
