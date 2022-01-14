import { Injectable } from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from '@angular/router';
import { Observable } from 'rxjs';
import {ProfilService} from "../../services/profil/profil.service";

@Injectable({
  providedIn: 'root'
})
export class AdminGuard implements CanActivate
{

    constructor(private profilService: ProfilService, private router: Router) {}


    canActivate( route: ActivatedRouteSnapshot, state: RouterStateSnapshot ): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree
    {
        if(this.profilService.getId() === -1) // si non connecté
        {
            this.router.navigateByUrl("/login");
            return false;
        }
        else {
            if(this.profilService.isAdmin()) return true;
            else {
                this.router.navigateByUrl("/login");
                return false;
            }
        }
    }
  
}
