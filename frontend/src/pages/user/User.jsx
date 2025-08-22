import React, { useState, useEffect } from 'react';
import axios from 'axios';

export function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/v1/user/');
        
        // Use o console.log() para ver a resposta completa da API
        console.log("Resposta completa da API:", response);
        
        // Especifique .data para ver apenas os dados recebidos
        console.log("Dados de usuários:", response.data);

        setUsers(response.data);
        setLoading(false);
      } catch (err) {
        console.error("Erro ao buscar usuários:", err);
        setError('Erro ao carregar usuários. Verifique se o servidor está rodando.');
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <p className="text-center text-gray-500">Carregando usuários...</p>;
  if (error) return <p className="text-center text-red-500 font-medium">{error}</p>;
  if (users.length === 0) return <p className="text-center text-gray-500">Nenhum usuário encontrado.</p>;

  return (
    <div className="p-6">
      <h2 className="text-center text-4xl font-extrabold text-blue-800 mb-8">Usuários da API</h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {users.map((user) => (
          <div
            key={user.id}
            className="bg-white shadow-md rounded-2xl p-6 border border-gray-200 hover:shadow-lg transition-shadow"
          >
            <p className="text-gray-700 font-semibold text-lg mb-2">
              <span className="font-medium text-gray-500">Nome:</span> {user.name}
            </p>
            <p className="text-gray-600 truncate">
              <span className="font-medium">Email:</span> {user.email}
            </p>
            <p className="text-gray-600">
              <span className="font-medium">Telefone:</span> {user.phone}
            </p>
            <p className="text-gray-600">
              <span className="font-medium">ID:</span> {user.id}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
