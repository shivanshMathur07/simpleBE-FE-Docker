import React from 'react';
const PeopleList = ({ people, onDelete }) => (
    <div style={{ marginTop: '2rem', width: '350px', marginLeft: 'auto', marginRight: 'auto' }}>
        <ul style={{ listStyle: 'none', padding: 0 }}>
            {people.map(person => (
                <li
                    key={person.id}
                    style={{
                        display: 'flex',
                        justifyContent: 'space-between',
                        alignItems: 'center',
                        padding: '0.5rem 0',
                        borderBottom: '1px solid #eee'
                    }}
                >
                    <span>{person.name} ({person.age})</span>
                    <button
                        onClick={() => onDelete(person._id)}
                        style={{
                            background: '#e74c3c',
                            color: '#fff',
                            border: 'none',
                            borderRadius: '4px',
                            padding: '0.3rem 0.7rem',
                            cursor: 'pointer'
                        }}
                    >
                        Delete
                    </button>
                </li>
            ))}
        </ul>
    </div>
);

export default PeopleList;