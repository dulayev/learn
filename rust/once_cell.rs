use std::cell::UnsafeCell;

pub struct OnceCell<T> {
    unsafe_cell: UnsafeCell<Option<T>>,
}

impl<T> OnceCell<T> {
    pub fn new() -> Self {
        Self {
            unsafe_cell: UnsafeCell::new(None),
        }
    }
    pub fn set(&self, val: T) -> Result<(), T> {
        let rm = unsafe { &mut *self.unsafe_cell.get() };
        if rm.is_some() {
            return Err(val);
        }
        *rm = Some(val);
        Ok(())
    }
    pub fn get(&self) -> Option<&T> {
        unsafe { &*self.unsafe_cell.get() }.as_ref()
    }
    pub fn get_or_init(&self, f: impl FnOnce() -> T) -> &T {
        if self.get().is_none() {
            assert!(self.set(f()).is_ok());
            // if f() called get_or_init or set, then this set will fail
            // that prevent wrong set after set
            // if allow set after set -> different refs might be returned
            // first is invalid
        }
        unsafe { &*self.unsafe_cell.get() }.as_ref().unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_once_cell() {
        let oc = OnceCell::<String>::new();
        assert!(oc.get() == None);
        assert!(oc.set(String::from("comprise")).is_ok());
        let rs = oc.get();
        assert!(rs.is_some());
        assert!("comprise" == rs.unwrap());
        assert!(oc.set(String::from("comprise")).is_err());

        let oc = OnceCell::<String>::new();
        assert!("holy" == oc.get_or_init(|| String::from("holy")));
    }

    #[test]
    #[should_panic]
    fn reentrance_test() {
        let mut rs: Option<&str> = None;
        let oc = OnceCell::<String>::new();
        let rs2 = oc.get_or_init(|| {
            rs = Some(&*oc.get_or_init(|| String::from("holy")));
            String::from("grave")
        });
        println!("{rs:?} {rs2}"); // if get_or_init doesn't panick rs has invalid value here
    }
}
