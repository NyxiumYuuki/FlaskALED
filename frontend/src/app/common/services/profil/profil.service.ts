import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProfilService
{

    constructor()
    {
        if(localStorage.getItem('id') === null) this.setId(-1);
        if(localStorage.getItem('isAdmin') === null) this.setIsAdmin(false);
    }

    getId(): number
    {
        let idString = localStorage.getItem('id');
        if(idString === null) return -1;
        else return parseInt(idString);
    }

    setId(id: number): void
    {
        localStorage.setItem('id', id.toString());
    }

    isAdmin(): boolean
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
