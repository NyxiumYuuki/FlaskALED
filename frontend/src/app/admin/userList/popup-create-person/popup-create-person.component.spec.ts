import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PopupCreatePersonComponent } from './popup-create-person.component';

describe('PopupCreerUtilisateurComponent', () => {
  let component: PopupCreatePersonComponent;
  let fixture: ComponentFixture<PopupCreatePersonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PopupCreatePersonComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PopupCreatePersonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
