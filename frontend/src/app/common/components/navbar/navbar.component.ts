import {Component, Input, OnInit} from '@angular/core';
import {ProfilService} from "../../services/profil/profil.service";

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit
{
    @Input() pour = "login";

    constructor(private profilService: ProfilService) { }

    ngOnInit(): void {}

    onDeconnexion(): void
    {
        this.profilService.setId(-1);
        this.profilService.setIsAdmin(false);
    }

}
