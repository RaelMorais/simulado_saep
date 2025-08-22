// src/rotas/AppRoutes.jsx

import { Routes, Route } from "react-router-dom";
import { Home } from "../pages/Home";
import { Users } from "../pages/user/User";

export function AppRoutes() {
    return (
        <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/user' element={<Users />} />
        </Routes>
    );
}
