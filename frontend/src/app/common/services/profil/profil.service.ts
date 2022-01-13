import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProfilService
{

    getId(): number | null
    {
        let idString = localStorage.getItem('id');
        if(idString === null) return null;
        else return parseInt(idString);
    }

    setId(id: number): void
    {
        localStorage.setItem('id', id.toString());
    }

    getIsAdmin(): boolean
    {
        let isAdminString = localStorage.getItem('isAdmin');
        if(isAdminString === "T") return true;
        else return false;
    }

    setIsAdmin(isAdmin: boolean): void
    {
        let isAdminString = "" ;
        if(isAdmin) isAdminString = "T";
        else isAdminString = "F";
        localStorage.setItem('isAdmin', isAdminString);
    }

}
